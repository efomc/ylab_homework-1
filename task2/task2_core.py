def int32_to_ip(int32):
    ipv_adress_list = []
    for octet_exponent in range(3, -1, -1):
        ipv_adress_list.append(str(int32 // 256**octet_exponent))
        int32 = int32 % 256**octet_exponent
    return ".".join(ipv_adress_list)
