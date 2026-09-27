import ipaddress


# ==========================================
#        IP ADDRESS INFORMATION TOOL
# ==========================================


def analyze_ip():

    ip_input = input("\nEnter IP Address/CIDR : ")

    try:

        # Convert input into IP interface object
        network = ipaddress.ip_interface(ip_input)

        # Get IP version
        ip_version = network.ip.version

        prefix_length = network.network.prefixlen


        # ==========================================
        #             IP INFORMATION
        # ==========================================

        print("\n" + "-" * 50)
        print("                IP INFORMATION")
        print("-" * 50)

        print(f"IP Address       : {network.ip}")
        print(f"IP Version       : IPv{ip_version}")
        print(f"CIDR Prefix      : /{prefix_length}")
        print(f"Subnet Mask      : {network.network.netmask}")
        print(f"Network Address  : {network.network.network_address}")

        # IPv4 has broadcast address
        if ip_version == 4:

            print(f"Broadcast Address: {network.network.broadcast_address}")

        else:

            print("Broadcast Address: Not Applicable")


        # ==========================================
        #             HOST INFORMATION
        # ==========================================

        total_addresses = network.network.num_addresses


        if ip_version == 4:

            # /32 = Single host
            if prefix_length == 32:

                usable_hosts = 1
                first_host = network.ip
                last_host = network.ip


            # /31 = Point-to-point network
            elif prefix_length == 31:

                usable_hosts = 2
                first_host = network.network.network_address
                last_host = network.network.broadcast_address


            # Normal IPv4 networks
            else:

                usable_hosts = total_addresses - 2
                first_host = network.network.network_address + 1
                last_host = network.network.broadcast_address - 1


            print("\n" + "-" * 50)
            print("                HOST INFORMATION")
            print("-" * 50)

            print(f"Total Addresses : {total_addresses}")
            print(f"Usable Hosts    : {usable_hosts}")
            print(f"First Host      : {first_host}")
            print(f"Last Host       : {last_host}")


        else:

            # IPv6 does not use IPv4-style broadcast
            print("\n" + "-" * 50)
            print("                HOST INFORMATION")
            print("-" * 50)

            print(f"Total Addresses : {total_addresses}")
            print("Usable Hosts    : N/A")
            print("First Host      : N/A")
            print("Last Host       : N/A")


        # ==========================================
        #               IP TYPE
        # ==========================================

        if network.ip.is_loopback:

            ip_type = "Loopback IP"

        elif network.ip.is_unspecified:

            ip_type = "Unspecified IP"

        elif network.ip.is_multicast:

            ip_type = "Multicast IP"

        elif network.ip.is_link_local:

            ip_type = "Link-Local IP"

        elif network.ip.is_private:

            ip_type = "Private IP"

        else:

            ip_type = "Public IP"


        print("\n" + "-" * 50)
        print("                  IP TYPE")
        print("-" * 50)

        print(f"IP Type         : {ip_type}")


        # ==========================================
        #              IP CLASS
        # ==========================================

        if ip_version == 4:

            first_octet = int(str(network.ip).split(".")[0])


            if 1 <= first_octet <= 126:

                ip_class = "Class A"


            elif 128 <= first_octet <= 191:

                ip_class = "Class B"


            elif 192 <= first_octet <= 223:

                ip_class = "Class C"


            elif 224 <= first_octet <= 239:

                ip_class = "Class D (Multicast)"


            elif 240 <= first_octet <= 255:

                ip_class = "Class E (Experimental)"


            else:

                ip_class = "Special"


            print(f"IP Class        : {ip_class}")


        else:

            print("IP Class        : Not Applicable")


        # ==========================================
        #             ANALYSIS COMPLETED
        # ==========================================

        print("\n" + "=" * 50)
        print("             ANALYSIS COMPLETED")
        print("=" * 50)


    except ValueError:

        print("\n" + "!" * 50)
        print("❌ Invalid IP Address or CIDR!")
        print("Example: 192.168.1.10/24")
        print("!" * 50)


# ==========================================
#                MAIN MENU
# ==========================================


def main():

    while True:

        print("\n" + "=" * 50)
        print("       IP ADDRESS INFORMATION TOOL")
        print("=" * 50)

        print("\n1. Analyze IP Address")
        print("2. Exit")


        choice = input("\nEnter your choice : ")


        # ==========================================
        #             ANALYZE IP
        # ==========================================

        if choice == "1":

            analyze_ip()


        # ==========================================
        #                  EXIT
        # ==========================================

        elif choice == "2":

            print("\n" + "=" * 50)
            print("       Thank you for using the tool!")
            print("=" * 50)

            break


        # ==========================================
        #             INVALID CHOICE
        # ==========================================

        else:

            print("\n❌ Invalid Choice!")
            print("Please select 1 or 2.")


# ==========================================
#              PROGRAM START
# ==========================================


if __name__ == "__main__":

    main()