# winget private repository

A Python implementation of a private winget repository server (/REST API).

## Setting up a local SSL certificate

`winget` only allows `https://` sources. This means that if we want to run
locally, then we need a self-signed SSL certificate for `localhost`.

[`localhost.pfx`](conf/localhost.pfx) can be used for this purpose. It was
created from [these instructions](https://gist.github.com/alicoskun/57acda07d5ab672a3c820da57b9531e3).
To install it, issue the following in a Powershell Admin prompt:

```bash
$password=ConvertTo-SecureString "12345" -asplaintext -force
Import-PfxCertificate -FilePath conf\localhost.pfx Cert:\LocalMachine\My -Password $password -Exportable
Import-Certificate -FilePath conf\localhost.cert -CertStoreLocation Cert:\CurrentUser\Root
```

To remove it later, run `mmc`, click `File/Add or Remove Snap-in` then
`Certificates/Add/My User account` then `Finish` and again for
`Computer account`. Then click `OK`. Then delete `localhost` expiring 2041 from
`Current User/Personal`, `Current User/Trusted Root Certification Authorities`,
and `Local Computer/Personal`.

### Set up the development environment

    pip install -Ur requirements/base-full.txt

### Run locally

    python manage.py runserver

Then:

    python sslproxy.py

Then you can add the REST source (note the `httpS`):

    winget source add -n wpr -a https://localhost:8443/api/ -t "Microsoft.Rest"

### Sniff Microsoft's implementation

Look at the `msstore` source shown by `winget source list`. Typically, it is:

    https://storeedgefd.dsx.mp.microsoft.com/v9.0

Start `sslproxy` as a man-in-the-middle proxy for the above domain:

    python sslproxy.py 8444 storeedgefd.dsx.mp.microsoft.com 443 

Then you can add the proxied source via:

    winget source add -n ms -a https://localhost:8444/v9.0 -t "Microsoft.Rest"

(Note that we used the path `/v9.0` from above.)

Now you can inspect the traffic in the output of `sslproxy` when you perform
`winget` commands.