import rsa


def create_keys() -> tuple[str, str]:
    """
        Generate keys, pub and priv for user
    :return:
    """
    public_key, private_key = rsa.newkeys(2048)
    return (public_key.save_pkcs1().decode(),
            private_key.save_pkcs1().decode())


def create_signature(private_key: str) -> bytes:
    return rsa.sign('Hi'.encode(),
                    rsa.PrivateKey.load_pkcs1(private_key.encode()),
                    'SHA-1')

