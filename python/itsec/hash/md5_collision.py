import hashlib

# Two different 128-byte messages with the same MD5 hash
message1 = bytes.fromhex(
    "d131dd02c5e6eec4693d9a0698aff95c"
    "2fcab58712467eab4004583eb8fb7f89"
    "55ad340609f4b30283e488832571415a"
    "085125e8f7cdc99fd91dbdf280373c5b"
    "d8823e3156348f5bae6dacd436c919c6"
    "dd53e2b487da03fd02396306d248cda0"
    "e99f33420f577ee8ce54b67080a80d1e"
    "c69821bcb6a8839396f9652b6ff72a70"
)

message2 = bytes.fromhex(
    "d131dd02c5e6eec4693d9a0698aff95c"
    "2fcab50712467eab4004583eb8fb7f89"
    "55ad340609f4b30283e4888325f1415a"
    "085125e8f7cdc99fd91dbd7280373c5b"
    "d8823e3156348f5bae6dacd436c919c6"
    "dd53e23487da03fd02396306d248cda0"
    "e99f33420f577ee8ce54b67080280d1e"
    "c69821bcb6a8839396f965ab6ff72a70"
)

hash1 = hashlib.md5(message1).hexdigest()
hash2 = hashlib.md5(message2).hexdigest()

print("Message 1 MD5:", hash1)
print("Message 2 MD5:", hash2)
print("")

print("Are the messages identical?", message1 == message2)
print("Are the MD5 hashes identical?", hash1 == hash2)


hash1_sha = hashlib.sha256(message1).hexdigest()
hash2_sha = hashlib.sha256(message2).hexdigest()

#print("")
#print("Message 1 SHA-256:", hash1_sha)
#print("Message 2 SHA-256:", hash2_sha)