from solders.keypair import Keypair
import base58

def generate_solana_wallets(num_wallets, pubkey_file="public_keys.txt", privkey_base58_file="private_keys_base58.txt", privkey_array_file="private_keys_array.txt"):
    # 存储生成的密钥信息
    public_keys = []
    private_keys_base58 = []
    private_keys_array = []
    
    # 生成指定数量的钱包
    for i in range(num_wallets):
        keypair = Keypair()
        public_key = str(keypair.pubkey())
        private_key_bytes = keypair.secret()  # 32 字节种子
        public_key_bytes = bytes(keypair.pubkey())  # 32 字节公钥
        full_secret_key = private_key_bytes + public_key_bytes  # 64 字节完整密钥
        private_key_base58 = base58.b58encode(full_secret_key).decode('ascii')
        private_key_array = str(list(full_secret_key))  # 字节数组格式
        
        public_keys.append(public_key)
        private_keys_base58.append(private_key_base58)
        private_keys_array.append(private_key_array)
        
        print(f"生成钱包 {i + 1}:")
        print(f"钱包地址 (公钥): {public_key}")
        print(f"私钥 (Base58): {private_key_base58}")
        print(f"私钥 (字节数组): {private_key_array}")
        print("请妥善保存私钥，不要泄露给任何人！")
        print("-" * 50)
    
    # 导出公钥到文件
    with open(pubkey_file, "w") as pub_file:
        for pubkey in public_keys:
            pub_file.write(f"{pubkey}\n")
    
    # 导出 Base58 私钥到文件
    with open(privkey_base58_file, "w") as priv_base58_file:
        for privkey in private_keys_base58:
            priv_base58_file.write(f"{privkey}\n")
    
    # 导出字节数组私钥到文件
    with open(privkey_array_file, "w") as priv_array_file:
        for privkey in private_keys_array:
            priv_array_file.write(f"{privkey}\n")
    
    print(f"已生成 {num_wallets} 个钱包")
    print(f"公钥已保存至: {pubkey_file}")
    print(f"私钥 (Base58) 已保存至: {privkey_base58_file}")
    print(f"私钥 (字节数组) 已保存至: {privkey_array_file}")

if __name__ == "__main__":
    # 设置生成钱包的数量
    num_wallets = int(input("请输入要生成的钱包数量: "))
    generate_solana_wallets(num_wallets)
