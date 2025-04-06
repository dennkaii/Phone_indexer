{
  pkgs,
  lib,
  config,
  inputs,
  ...
}: {
  env = {
    NIX_LD_LIBRARY_PATH = lib.makeLibraryPath (
      with pkgs; [
        zlib
        libgcc # Pandas, numpy etc.
        stdenv.cc.cc
      ]
    );
    GREET = "[python env test]";
  };
  # https://devenv.sh/packages/
  packages = with pkgs; [
    postgresql
    firefox-unwrapped
    geckodriver
    gcc-unwrapped # fix: libstdc++.so.6: cannot open shared object file
    libz # fix: for numpy/pandas import
  ];

  languages.python = {
    enable = true;

    uv = {
      enable = true;
    };
    venv.enable = true;
    venv.requirements = ./requirements.txt;
  };
  # https://devenv.sh/scripts/
  scripts.hello.exec = ''
    echo hello from $GREET
  '';

  enterShell = ''
    echo $GREET
    git --version
  '';
  # https://devenv.sh/tests/
  enterTest = ''
    echo "Running tests"
    git --version | grep --color=auto "${pkgs.git.version}"
  '';

  # https://devenv.sh/git-hooks/
  # git-hooks.hooks.shellcheck.enable = true;

  # See full reference at https://devenv.sh/reference/options/
}
