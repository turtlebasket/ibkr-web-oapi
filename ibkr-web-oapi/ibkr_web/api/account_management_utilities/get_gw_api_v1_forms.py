from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_detail_response import ProblemDetailResponse
from ...models.user_name_available_response import UserNameAvailableResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    form_no: Union[Unset, List[int]] = UNSET,
    get_docs: Union[Unset, str] = UNSET,
    from_date: Union[Unset, str] = UNSET,
    to_date: Union[Unset, str] = UNSET,
    language: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_form_no: Union[Unset, List[int]] = UNSET
    if not isinstance(form_no, Unset):
        json_form_no = form_no

    params["formNo"] = json_form_no

    params["getDocs"] = get_docs

    params["fromDate"] = from_date

    params["toDate"] = to_date

    params["language"] = language

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/gw/api/v1/forms",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ProblemDetailResponse, UserNameAvailableResponse]]:
    if response.status_code == 400:
        response_400 = ProblemDetailResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = ProblemDetailResponse.from_dict(response.json())

        return response_403
    if response.status_code == 500:
        response_500 = ProblemDetailResponse.from_dict(response.json())

        return response_500
    if response.status_code == 200:
        response_200 = UserNameAvailableResponse.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = ProblemDetailResponse.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ProblemDetailResponse, UserNameAvailableResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    form_no: Union[Unset, List[int]] = UNSET,
    get_docs: Union[Unset, str] = UNSET,
    from_date: Union[Unset, str] = UNSET,
    to_date: Union[Unset, str] = UNSET,
    language: Union[Unset, str] = UNSET,
) -> Response[Union[ProblemDetailResponse, UserNameAvailableResponse]]:
    """Get forms

     Get forms<br><br>**Scope**: `accounts.read` OR `forms.read`<br>**Security Policy**: `HTTPS`

    Args:
        form_no (Union[Unset, List[int]]):
        get_docs (Union[Unset, str]):
        from_date (Union[Unset, str]):
        to_date (Union[Unset, str]):
        language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetailResponse, UserNameAvailableResponse]]
    """

    kwargs = _get_kwargs(
        form_no=form_no,
        get_docs=get_docs,
        from_date=from_date,
        to_date=to_date,
        language=language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    form_no: Union[Unset, List[int]] = UNSET,
    get_docs: Union[Unset, str] = UNSET,
    from_date: Union[Unset, str] = UNSET,
    to_date: Union[Unset, str] = UNSET,
    language: Union[Unset, str] = UNSET,
) -> Optional[Union[ProblemDetailResponse, UserNameAvailableResponse]]:
    """Get forms

     Get forms<br><br>**Scope**: `accounts.read` OR `forms.read`<br>**Security Policy**: `HTTPS`

    Args:
        form_no (Union[Unset, List[int]]):
        get_docs (Union[Unset, str]):
        from_date (Union[Unset, str]):
        to_date (Union[Unset, str]):
        language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetailResponse, UserNameAvailableResponse]
    """

    return sync_detailed(
        client=client,
        form_no=form_no,
        get_docs=get_docs,
        from_date=from_date,
        to_date=to_date,
        language=language,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    form_no: Union[Unset, List[int]] = UNSET,
    get_docs: Union[Unset, str] = UNSET,
    from_date: Union[Unset, str] = UNSET,
    to_date: Union[Unset, str] = UNSET,
    language: Union[Unset, str] = UNSET,
) -> Response[Union[ProblemDetailResponse, UserNameAvailableResponse]]:
    """Get forms

     Get forms<br><br>**Scope**: `accounts.read` OR `forms.read`<br>**Security Policy**: `HTTPS`

    Args:
        form_no (Union[Unset, List[int]]):
        get_docs (Union[Unset, str]):
        from_date (Union[Unset, str]):
        to_date (Union[Unset, str]):
        language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetailResponse, UserNameAvailableResponse]]
    """

    kwargs = _get_kwargs(
        form_no=form_no,
        get_docs=get_docs,
        from_date=from_date,
        to_date=to_date,
        language=language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    form_no: Union[Unset, List[int]] = UNSET,
    get_docs: Union[Unset, str] = UNSET,
    from_date: Union[Unset, str] = UNSET,
    to_date: Union[Unset, str] = UNSET,
    language: Union[Unset, str] = UNSET,
) -> Optional[Union[ProblemDetailResponse, UserNameAvailableResponse]]:
    """Get forms

     Get forms<br><br>**Scope**: `accounts.read` OR `forms.read`<br>**Security Policy**: `HTTPS`

    Args:
        form_no (Union[Unset, List[int]]):
        get_docs (Union[Unset, str]):
        from_date (Union[Unset, str]):
        to_date (Union[Unset, str]):
        language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetailResponse, UserNameAvailableResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_no=form_no,
            get_docs=get_docs,
            from_date=from_date,
            to_date=to_date,
            language=language,
        )
    ).parsed
