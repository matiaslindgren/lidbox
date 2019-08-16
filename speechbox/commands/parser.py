from speechbox.commands import ExpandAbspath
from speechbox.commands.base import Command
import speechbox.dataset as dataset


class Parser(Command):
    tasks = ("parse",)

    @classmethod
    def create_argparser(cls, subparsers):
        parser = super().create_argparser(subparsers)
        parser.add_argument("src",
            type=str,
            action=ExpandAbspath,
            help="Parse files from this directory.")
        parser.add_argument("dst",
            type=str,
            action=ExpandAbspath,
            help="Save parsed output into this directory.")
        parser.add_argument("--parse",
            choices=dataset.all_parsers,
            help="Parse from --src to --dst using the given dataset parser.")
        parser.add_argument("--resample",
            type=int,
            help="Resample all output files to the given sample frequency.")
        return parser

    def parse(self):
        args = self.args
        if args.verbosity:
            print("Parsing dataset '{}'".format(args.parse))
        if not (self.args_src_ok() and self.args_dst_ok()):
            return 1
        parser_config = {
            "dataset_root": args.src,
            "output_dir": args.dst,
        }
        if args.resample:
            parser_config["resampling_freq"] = args.resample
        parser = dataset.get_dataset_parser(args.parse, parser_config)
        num_parsed = 0
        if not args.verbosity:
            for _ in parser.parse():
                num_parsed += 1
        else:
            for output in parser.parse():
                num_parsed += 1
                if any(output):
                    status, out, err = output
                    msg = "Warning:"
                    if status:
                        msg += " exit code: {}".format(status)
                    if out:
                        msg += " stdout: '{}'".format(out)
                    if err:
                        msg += " stderr: '{}'".format(err)
                    print(msg)
        print(num_parsed, "files parsed from '{}' to '{}'".format(args.src, args.dst))

    def run(self):
        super().run()
        return self.run_tasks()