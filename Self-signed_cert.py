from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from datetime import datetime
from datetime import timedelta
from  os.path import expanduser

home = expanduser("~")
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=4096,
    backend=default_backend()
)

with open(home+'/test_key.pem', "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(b"passphrase"),
    ))

subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"DC"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"Washington"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"RavRic Solutions"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"www.myjourneytoself.com"),
 ])
cert = x509.CertificateBuilder().subject_name(
    subject).issuer_name(
    issuer
    ).public_key(
    private_key.public_key()
    ).serial_number(
    x509.random_serial_number()
    ).not_valid_before(
    datetime.utcnow()
    ).not_valid_after(
    # Our certificate will be valid for 10 days
    datetime.utcnow() + timedelta(days=10)
    ).add_extension(
     x509.SubjectAlternativeName([x509.DNSName(u"localhost")]),
     critical=False,
# Sign our certificate with our private key
    ).sign(private_key, hashes.SHA256(), default_backend())
# Write our certificate out to disk.
with open(home+'/root_certificate.pem', "wb") as f:
     f.write(cert.public_bytes(serialization.Encoding.PEM))