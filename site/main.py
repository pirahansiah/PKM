#!/usr/bin/env python3

from __future__ import annotations

import sys

from knowledge_graph import main as knowledge_graph_main


def main() -> int:
	"""Run the knowledge graph pipeline."""
	return knowledge_graph_main()


if __name__ == "__main__":
	sys.exit(main())
