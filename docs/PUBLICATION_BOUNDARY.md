# Publication boundary

The public edition is safe only when every committed file fits one of these
categories.

## Allowed

- provider-neutral source code;
- tests, examples, and build metadata;
- sanitized architecture and maintainer documentation;
- public contribution, security, and licensing files;
- synthetic fixtures with no personal or operational data.

## Excluded

- credentials, tokens, keys, cookies, and session data;
- personal records, correspondence, private prompts, and recovery material;
- local filesystem paths and private runtime logs;
- financial, trading, tax, or broker data;
- raw exports, databases, and large data archives;
- private infrastructure or operational identifiers.

Before every public release, review the complete tree and history of the target
public repository. Do not assume that a private source repository's ignore
rules remove material from its existing Git history.
