"""Hardware configuration dict."""

import types

flash_command = 'vendor/flashrom -p internal -w {0} --ifd -i bios'
overrider_command = 'vendor/flashrom -p internal:boardmismatch=force -w {0} --ifd -i bios'

vpxxxx_flash_command = 'vendor/flashrom -p internal -w {0}'
vpxxxx_upgrade = 'vendor/flashrom -p internal -w {0} --fmap -i RW_SECTION_A'


CONFIGURATIONS = types.MappingProxyType({
    'fw2': {
        'cpu': 'J1800',
        'bios': [
            {
                'vendor': 'ami',
                'file': 'FW2_BTL4A012.bin',
            },
        ],
        'command': flash_command,
    },
    'fw2b': {
        'cpu': 'J3060',
        'bios': [
            {
                'vendor': 'ami',
                'file': 'FW2B_BSW4L011.bin',
            },
            {
                'vendor': 'coreboot',
                'file': 'protectli_fw2b_v4.9.0.2.rom',
            },
        ],
        'command': flash_command,
    },
    'fw1': {
        'cpu': 'J1900',
        'bios': [
            {
                'vendor': 'ami',
                'file': 'FW1_BTL4A012.bin',
            },
        ],
        'command': flash_command,
    },
    'fw4a': {
        'cpu': 'E3845',
        'bios': [
            {
                'vendor': 'ami',
                'file': 'FW4A_E38L4A12.bin',
            },
        ],
        'command': flash_command,
    },
    'fw4b': {
        'cpu': 'J3160',
        'bios': [
            {
                'vendor': 'ami',
                'file': 'FW4B_BSW4L011.bin',
            },
            {
                'vendor': 'coreboot',
                'file': 'protectli_fw4b_v4.12.0.7.rom',
            },
        ],
        'command': flash_command,
    },
    'fw4c': {
        'cpu': 'J3710',
        'bios': [
            {
                'vendor': 'ami',
                'file': 'FW4C_220921.bin',
            },
        ],
        'command': flash_command,
    },
    'fw6a': {
        'cpu': '3865U',
        'bios': [
            {
                'vendor': 'ami',
                'file': 'FW6_all_YKBR6L12.bin',
            },
            {
                'vendor': 'coreboot',
                'file': 'protectli_all_fw6_vault_kbl_v1.0.14.rom',
            },
        ],
        'command': flash_command,
    },

    'fw6ar': {
        'cpu': '3867U',
        'bios': [
            {
                'vendor': 'ami',
                'file': 'FW6_all_YKBR6L12.bin',
            },
            {
                'vendor': 'coreboot',
                'file': 'protectli_all_fw6_vault_kbl_v1.0.14.rom',
            },
        ],
        'command': flash_command,
    },
    'fw6b': {
        'cpu': '7100U',
        'bios': [
            {
                'vendor': 'ami',
                'file': 'FW6_all_YKBR6L12.bin',
            },
            {
                'vendor': 'coreboot',
                'file': 'protectli_all_fw6_vault_kbl_v1.0.14.rom',
            },
        ],
        'command': flash_command,
    },
    'fw6br': {
        'cpu': '7020U',
        'bios': [
            {
                'vendor': 'ami',
                'file': 'FW6_all_YKBR6L12.bin',
            },
            {
                'vendor': 'coreboot',
                'file': 'protectli_all_fw6_vault_kbl_v1.0.14.rom',
            },
        ],
        'command': flash_command,
    },
    'fw6br2': {
        'cpu': '8130U',
        'bios': [
            {
                'vendor': 'ami',
                'file': 'FW6_all_YKBR6L12.bin',
            },
            {
                'vendor': 'coreboot',
                'file': 'protectli_all_fw6_vault_kbl_v1.0.14.rom',
            },
        ],
        'command': flash_command,
    },
    'fw6c': {
        'cpu': '7200U',
        'bios': [
            {
                'vendor': 'ami',
                'file': 'FW6_all_YKBR6L12.bin',
            },
            {
                'vendor': 'coreboot',
                'file': 'protectli_all_fw6_vault_kbl_v1.0.14.rom',
            },
        ],
        'command': flash_command,
    },
    'fw6m': {
        'cpu': 'FW6MC',
        'bios': [
            {
                'vendor': 'ami',
                'file': 'FW6_825_KBU6LA09.bin',
            },
            {
                'vendor': 'coreboot',
                'file': 'protectli_all_fw6_vault_kbl_v1.0.14.rom',
            },
        ],
        'command': flash_command,
    },
    'fw6d': {
        'cpu': '8250U',
        'bios': [
            {
                'vendor': 'ami',
                'file': 'FW6_all_YKBR6L12.bin',
            },
            {
                'vendor': 'coreboot',
                'file': 'protectli_all_fw6_vault_kbl_v1.0.14.rom',
            },
        ],
        'command': flash_command,
        'override': overrider_command,
    },
    'fw6e': {
        'cpu': '8550U',
        'bios': [
            {
                'vendor': 'ami',
                'file': 'FW6_all_YKBR6L12.bin',
            },
            {
                'vendor': 'coreboot',
                'file': 'protectli_all_fw6_vault_kbl_v1.0.14.rom',
            },
        ],
        'command': flash_command,
        'override': overrider_command,
    },
    'vp2410': {
        'cpu': 'J4125',
        'bios': [
            {
                'vendor': 'ami',
                'file': 'VP2410_GLK4L260.bin', 
            },
            {
                'vendor': 'coreboot',
                'file': 'protectli_vp2410_DF_1.0.9.rom',

            },
        ],
        'command': vpxxxx_flash_command,
    },
    'vp2410r': {
        'cpu': 'J4125',
        'bios': [
            {
                'vendor': 'ami',
                'file': 'VP2410_GML4AV30.bin',
            },
            {
                'vendor': 'coreboot',
                'file': 'protectli_vp2410_DF_v1.0.15.rom',
            },
        ],
        'command': vpxxxx_flash_command,
    },
    'vp4630': {
        'cpu': '10110U',
        'bios': [
            {
                'vendor': 'ami',

                'file': 'vp4630_YW6L2314.bin',

                
            },
            {
                'vendor': 'coreboot',
                'file': 'protectli_vp4630_v1.0.17.rom',
            },

        ],
        'command': vpxxxx_flash_command,
        'upgrade': vpxxxx_upgrade,
    }
     'vp4650': {
        'cpu': '10210U',
        'bios': [
            {
                'vendor': 'ami',
                'file': 'vp4650_YW6L2514.bin',
                
            },

        ],
        'command': vpxxxx_flash_command,
        'upgrade': vpxxxx_upgrade,
    },

})
