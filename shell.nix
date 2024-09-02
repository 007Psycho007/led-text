
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "data-science";
  packages = with pkgs; [
    mpremote
    (python311.withPackages (ps: with ps; [
      mpremote
    ]))
    nodejs
    (vscode-with-extensions.override {
        vscodeExtensions = with vscode-extensions; [
          ms-python.python
          ms-toolsai.jupyter
        ] ++ pkgs.vscode-utils.extensionsFromVscodeMarketplace [
      {
        name = "wokwi-vscode";
        publisher = "Wokwi";
        version = "2.5.2";
        sha256 = "GYIZN+mPFV+XsskVScXJAZpeXai66QwX0juIMMR5dzA=";
      }
    ];
      })
  ];
}
