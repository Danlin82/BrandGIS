@echo off
call "C:\OSGeo4W\bin\o4w_env.bat"
call "C:\OSGeo4W\bin\qt5_env.bat"
call "C:\OSGeo4W\bin\py3_env.bat"

@echo on
C:\OSGeo4W\apps\Python39\Scripts\pyrcc5 -o resources.py resources.qrc
pause