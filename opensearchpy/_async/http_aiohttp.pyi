# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.
#
#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

from typing import Any, Collection, Mapping, Optional, Tuple, Union

from ..connection import Connection
from ._extra_imports import aiohttp  # type: ignore[attr-defined,unused-ignore]# noqa

class AsyncConnection(Connection):
    async def perform_request(  # type: ignore[attr-defined,unused-ignore]# noqa
        self,
        method: str,
        url: str,
        params: Optional[Mapping[str, Any]] = ...,
        body: Optional[bytes] = ...,
        timeout: Optional[Union[int, float]] = ...,
        ignore: Collection[int] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Tuple[int, Mapping[str, str], str]: ...
    async def close(self) -> None: ...

class AIOHttpConnection(AsyncConnection):
    session: Optional[aiohttp.ClientSession]
    ssl_assert_fingerprint: Optional[str]
    def __init__(
        self,
        host: str = ...,
        port: Optional[int] = ...,
        http_auth: Optional[Any] = ...,
        use_ssl: bool = ...,
        verify_certs: bool = ...,
        ssl_show_warn: bool = ...,
        ca_certs: Optional[Any] = ...,
        client_cert: Optional[Any] = ...,
        client_key: Optional[Any] = ...,
        ssl_version: Optional[Any] = ...,
        ssl_assert_fingerprint: Optional[Any] = ...,
        maxsize: int = ...,
        headers: Optional[Mapping[str, str]] = ...,
        ssl_context: Optional[Any] = ...,
        http_compress: Optional[bool] = ...,
        opaque_id: Optional[str] = ...,
        loop: Any = ...,
        **kwargs: Any,
    ) -> None: ...
