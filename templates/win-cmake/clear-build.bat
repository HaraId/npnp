@echo off

cd %~dp0

if exist build rd /s /q build
if exist bin rd /s /q bin
