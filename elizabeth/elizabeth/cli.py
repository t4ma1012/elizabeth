import argparse

def cmd_ingest(args):
    print("Not implemented yet")

def cmd_analyze(args):
    print("Not implemented yet")

def cmd_report(args):
    print("Not implemented yet")

def main():
    parser = argparse.ArgumentParser(
        prog="elizabeth",
        description="DFIR investigation tool for correlating Windows Event Logs and PCAP captures"
    )
    subparsers = parser.add_subparsers(title="commands", dest="command")
    subparsers.required = True

    # ingest
    p_ingest = subparsers.add_parser("ingest", help="Ingest EVTX and/or PCAP files into the database")
    p_ingest.add_argument("--evtx", type=str, help="Path to .evtx file")
    p_ingest.add_argument("--pcap", type=str, help="Path to .pcap file")
    p_ingest.set_defaults(func=cmd_ingest)

    # analyze
    p_analyze = subparsers.add_parser("analyze", help="Run detection and enrichment on ingested data")
    p_analyze.add_argument("--case", type=str, default="elizabeth.db", help="Path to case database")
    p_analyze.set_defaults(func=cmd_analyze)

    # report
    p_report = subparsers.add_parser("report", help="Generate HTML investigation report")
    p_report.add_argument("--output", type=str, default="report.html", help="Output file path")
    p_report.set_defaults(func=cmd_report)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()