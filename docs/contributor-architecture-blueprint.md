# Contributor architecture

The public repository is a static generated catalog. Its JSON catalog is the
machine-readable source for the README; the local validator checks the schema
and the shared CI runs that validator through pre-commit and pytest.
