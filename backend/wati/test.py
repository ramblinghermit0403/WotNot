from passlib.context import CryptContext

# Create a new context with bcrypt
pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated="auto")

# Generate a hash
hashed = pwd_cxt.hash("mysecretpassword")
print("Hashed password:", hashed)

# Verify the hash
is_valid = pwd_cxt.verify("mysecretpassword", hashed)
print("Password valid:", is_valid)
