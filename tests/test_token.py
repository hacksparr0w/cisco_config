from io import StringIO
from textwrap import dedent

import pytest

from cisco_config.token import Eol, Comment, Word, token_reader


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            """
            : Saved

            : 
            : Hardware:   FPR-2110
            :
            ASA Version 9.18(4)40 <context>

            hostname Router11
             !
             interface FastEthernet0/0
              ip address 192.168.10.1 255.255.255.0

            !--- Connected to Router21.

             !
             interface FastEthernet0/1
              ip address 172.16.11.1 255.255.255.0

            !--- Connected to PIX1.

             !
             router ospf 1
              log-adjacency-changes
              network 192.168.10.0 0.0.0.255 area 0
              default-information originate metric 5 route-map check-default
            """,
            (
                Eol(),
                Comment(content=" Saved"),
                Eol(),
                Eol(),
                Comment(content=" "),
                Eol(),
                Comment(content=" Hardware:   FPR-2110"),
                Eol(),
                Comment(content=""),
                Eol(),
                Word(value="ASA"),
                Word(value="Version"),
                Word(value="9.18(4)40"),
                Word(value="<context>"),
                Eol(),
                Eol(),
                Word(value="hostname"),
                Word(value="Router11"),
                Eol(),
                Comment(content=""),
                Eol(),
                Word(value="interface"),
                Word(value="FastEthernet0/0"),
                Eol(),
                Word(value="ip"),
                Word(value="address"),
                Word(value="192.168.10.1"),
                Word(value="255.255.255.0"),
                Eol(),
                Eol(),
                Comment(content="--- Connected to Router21."),
                Eol(),
                Eol(),
                Comment(content=""),
                Eol(),
                Word(value="interface"),
                Word(value="FastEthernet0/1"),
                Eol(),
                Word(value="ip"),
                Word(value="address"),
                Word(value="172.16.11.1"),
                Word(value="255.255.255.0"),
                Eol(),
                Eol(),
                Comment(content="--- Connected to PIX1."),
                Eol(),
                Eol(),
                Comment(content=""),
                Eol(),
                Word(value="router"),
                Word(value="ospf"),
                Word(value="1"),
                Eol(),
                Word(value="log-adjacency-changes"),
                Eol(),
                Word(value="network"),
                Word(value="192.168.10.0"),
                Word(value="0.0.0.255"),
                Word(value="area"),
                Word(value="0"),
                Eol(),
                Word(value="default-information"),
                Word(value="originate"),
                Word(value="metric"),
                Word(value="5"),
                Word(value="route-map"),
                Word(value="check-default"),
                Eol()
            )
        )
    ]
)
def test(input, expected):
    assert tuple(token_reader(StringIO(dedent(input)))) == expected
