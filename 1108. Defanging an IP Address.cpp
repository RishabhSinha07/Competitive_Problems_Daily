// Given a valid (IPv4) IP address, return a defanged version of that IP address.

// A defanged IP address replaces every period "." with "[.]".

class Solution
{
public:
    string defangIPaddr(string address)
    {
        string final;
        for (int i = 0; i < address.size(); i++)
        {
            if (address[i] == '.')
            {
                final += "[.]";
            }
            else
            {
                final += address[i];
            }
        }
        return final;
    }
};

// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Defanging an IP Address.
// Memory Usage: 5.9 MB, less than 74.28% of C++ online submissions for Defanging an IP Address.