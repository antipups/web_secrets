import rsa


def create_keys() -> tuple[str, str]:
    """
        Generate keys, pub and priv for user
    :return:
    """
    public_key, private_key = rsa.newkeys(512)
    return (public_key.save_pkcs1().decode(),
            private_key.save_pkcs1().decode())


signature_message = 'Hi'.encode()


def create_signature(private_key: str) -> bytes:
    """
        Создание сигнатуры по которой будем проверять в будущем ключики
    :param private_key: приватный ключ пользователя
    :return: сигнатура в байтах
    """
    return rsa.sign(signature_message,
                    rsa.PrivateKey.load_pkcs1(private_key.encode()),
                    'SHA-1')


def check_signature(public_key: str, signature: bytes) -> str | Exception:
    """
        Проверка сигнатуры
    :param public_key: публичный ключ пользователя
    :param signature: сигнатура
    :return: метод которым была проведена подпись, если всё ок то строка, иначе эксепшин
    """
    verify = bool(rsa.verify(signature_message,
                             signature,
                             rsa.PublicKey.load_pkcs1(public_key.encode())))
    if verify:
        return public_key


def check_keys_valid(private_key: str, public_key: str) -> bool | Exception:
    """
        Проверка ключей которые ввел пользователь, мб они битые
    :param private_key:
    :param public_key:
    :return: истина если всё ок
    """
    sign = create_signature(private_key=private_key)
    check_signature(public_key=public_key,
                    signature=sign)
    return True

