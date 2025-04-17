"""
csvtree – Transform flat CSV data into deep, hierarchical JSON structures.

CSVTree provides a Pythonic interface and custom JSONPath-inspired DSL
for defining mapping rules that convert rows and columns of a CSV file
into richly nested JSON objects and arrays.

Key Features:
- Declarative mapping: Use intuitive JSONPath-like expressions to specify
  how CSV columns should be placed within nested objects and lists.
- Flexible grouping: Aggregate rows into arrays or subtrees based on key fields.
- Pluggable parsers: Swap between the built‑in CSV parser or third‑party libraries
  (e.g., pandas) for performance and scalability.
- Output options: Emit minified or pretty‑printed JSON, with full control
  over encoding and formatting.

Getting Started:
    >>> from csvtree import Transformer
    >>> rules = {
    ...     "$.users[*]": {
    ...         "id": "$.user_id",
    ...         "profile": {
    ...             "name": "$.user_name",
    ...             "email": "$.user_email"
    ...         },
    ...         "orders[]": {
    ...             "order_id": "$.order_id",
    ...             "amount": "$.order_total"
    ...         }
    ...     }
    ... }
    >>> transformer = Transformer(mapping_rules=rules)
    >>> json_output = transformer.from_csv("data/users.csv")
    >>> print(json_output)

Modules
-------
csvtree.parser
    Core CSV parsing utilities.
csvtree.dsl
    JSONPath‑inspired DSL parser and interpreter.
csvtree.engine
    Transformation engine applying mapping rules.
csvtree.writer
    JSON generation and output formatting.

For detailed usage, examples, and advanced configuration, see the
project documentation at https://github.com/your-org/CSVTree.
"""