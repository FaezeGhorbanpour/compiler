java org.antlr.v4.Tool %1.g4 -visitor
javac %1*.java
java org.antlr.v4.gui.TestRig %1 s -gui