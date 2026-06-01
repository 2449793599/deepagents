"""Provider-specific MCP OAuth dispatch.

`resolve_provider(url)` returns the registered policy whose `matches`
predicate fires for `url`, with `GenericProvider` as the fallback.
"""

from libs.code.deepagents_code.mcp_providers._registry import resolve_provider
from libs.code.deepagents_code.mcp_providers.base import (
    GenericProvider,
    LoginResult,
    OAuthProvider,
)
from libs.code.deepagents_code.mcp_providers.github import GitHubProvider
from libs.code.deepagents_code.mcp_providers.slack import SlackProvider

__all__ = [
    "GenericProvider",
    "GitHubProvider",
    "LoginResult",
    "OAuthProvider",
    "SlackProvider",
    "resolve_provider",
]
