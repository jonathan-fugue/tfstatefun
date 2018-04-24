#!/usr/bin/env python

import sys
import os
import json
from jinja2 import Environment

STATE = """
{
    "version": 3,
    "terraform_version": "0.11.7",
    "serial": 1,
    "lineage": "f9f85a56-0ed5-7c93-f857-df04c1626ced",
    "modules": [
        {
            "path": [
                "root"
            ],
            "outputs": {},
            "resources": {
                "aws_vpc.main": {
                    "type": "aws_vpc",
                    "depends_on": [],
                    "primary": {
                        "id": "{{ vpc_id }}",
                        "attributes": {
                            "assign_generated_ipv6_cidr_block": "false",
                            "cidr_block": "{{ cidr }}",
                            "default_network_acl_id": "{{ na_id }}",
                            "default_route_table_id": "{{ rt_id }}",
                            "default_security_group_id": "{{ sg_id }}",
                            "dhcp_options_id": "{{ dhcp_id }}",
                            "enable_classiclink": "false",
                            "enable_classiclink_dns_support": "false",
                            "enable_dns_hostnames": "false",
                            "enable_dns_support": "true",
                            "id": "{{ vpc_id }}",
                            "instance_tenancy": "default",
                            "main_route_table_id": "{{ rt_id }}",
                            "tags.%": "1",
                            "tags.Env": "prod"
                        },
                        "meta": {
                            "schema_version": "1"
                        },
                        "tainted": false
                    },
                    "deposed": [],
                    "provider": "provider.aws"
                }
            },
            "depends_on": []
        }
    ]
}
"""

def main(args):
    try:
        if sys.stdin.isatty() and len(args) == 2:
            f = open(sys.argv[1], "r")
        elif not sys.stdin.isatty():
            f = sys.stdin
        else:
            usage()
    except FileNotFoundError:
        sys.exit('File not found')

    data = json.load(f)
    f.close()

    vpcs = data.get('resources', {}).get('vpcs', {})

    for _, top_level_vpc in vpcs.items():
        vpc_id = top_level_vpc['value']['vpc']['VpcId']
        cidr = top_level_vpc['value']['vpc']['CidrBlock']
        dhcp_id = top_level_vpc['value']['vpc']['DhcpOptionsId']
        rt_id = top_level_vpc['value']['defaultRouteTable']
        na_id = top_level_vpc['value']['defaultNetworkAcl']
        sg_id = top_level_vpc['value']['defaultSecurityGroup']

    print(
        Environment().from_string(STATE).render(
            vpc_id=vpc_id,
            cidr=cidr,
            dhcp_id=dhcp_id,
            rt_id=rt_id,
            na_id=na_id,
            sg_id=sg_id
        )
    )
      
def usage():
    print(__doc__)
    sys.exit(1)

if __name__ == "__main__":
    main(sys.argv)
