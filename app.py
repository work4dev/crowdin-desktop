# Compilation mode, support OS-specific options
# nuitka-project-if: {OS} in ("Linux", "Darwin", "FreeBSD"):
#    nuitka-project: --output-filename=crowdin-desktop
# nuitka-project-else:
#    nuitka-project: --output-filename=crowdin-desktop.exe

# nuitka-project: --onefile
# nuitka-project: --output-dir=output
# nuitka-project: --windows-disable-console

# The PySide6 plugin covers qt-plugins
# nuitka-project: --enable-plugin=pyside6
# nuitka-project: --include-qt-plugins=qml

from crowdin_desktop import main

if __name__ == "__main__":
    main()
