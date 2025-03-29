from eth_account import Account
import secrets

def generate_eth_wallets(num_wallets, address_file="eth_addresses.txt", privkey_file="eth_private_keys.txt"):
    # 存储生成的地址和私钥
    addresses = []
    private_keys = []
    
    # 生成指定数量的钱包
    for i in range(num_wallets):
        # 生成随机私钥
        private_key = "0x" + secrets.token_hex(32)  # 32 字节私钥，带 "0x" 前缀
        account = Account.from_key(private_key)  # 从私钥生成账户
        address = account.address  # 获取以太坊地址
        
        addresses.append(address)
        private_keys.append(private_key)
        
        print(f"生成钱包 {i + 1}:")
        print(f"钱包地址: {address}")
        print(f"私钥: {private_key}")
        print("请妥善保存私钥，不要泄露给任何人！")
        print("-" * 50)
    
    # 导出地址到文件
    with open(address_file, "w") as addr_file:
        for addr in addresses:
            addr_file.write(f"{addr}\n")
    
    # 导出私钥到文件
    with open(privkey_file, "w") as priv_file:
        for privkey in private_keys:
            priv_file.write(f"{privkey}\n")
    
    print(f"已生成 {num_wallets} 个以太坊钱包")
    print(f"地址已保存至: {address_file}")
    print(f"私钥已保存至: {privkey_file}")

if __name__ == "__main__":
    # 设置生成钱包的数量
    num_wallets = int(input("请输入要生成的以太坊钱包数量: "))
    generate_eth_wallets(num_wallets)
