grammar Contract;



// Lexer Rules
LOWERCASE : 'a'..'z';
DOUBLE : 'Double' ;
INT : 'Int' ;
DATE : 'Date';
CONTRACT : 'Contract' ;
NUMBER : '0'..'9'+;
LOWERCASE_NUMBER :('a'..'z' | '0'..'9');
PLUS : '+' ;
MINUS : '-' ;
TIMES : '*' ;
DIV : '/';
AND : 'and' ;
OR : 'or' ;
THEN : 'then' ;
SCALAX : 'scalaX' ;
SCALA : 'scala' ;
TRUNCATE : 'truncate' ;
TO : '->';
ASSIGNMENT : '::';
LPAREN : '(' ;
RPAREN : ')' ;
ONE : 'one' ;
COMMA : ',' ;
DOT : '.' ;
EQUAL : '=' ;
TIMEFUNCT : 'TimeFunct' ;
MKDATE : 'mkDate' ;
GIVE : 'give' ;
WS : [ \t\r\n]+ -> skip ;


// Parser Rules

program : (Assign | Funccall | Def )+ ;
Name : LOWERCASE LOWERCASE_NUMBER*;
Type : (INT | DOUBLE  | DATE | CONTRACT);
Operands : (PLUS | MINUS | DIV | TIMES) ;
Deffunc : LPAREN Type (COMMA Type)*  RPAREN TO Type ;
Defvar : Type ;
Def : Name ASSIGNMENT (Defvar | Deffunc)
	 | TIMEFUNCT LPAREN Deffunc RPAREN ;
Assign : Name EQUAL  Expr ;
Int : Name
	| NUMBER+ ;
Double : Name
	   | NUMBER+ DOT NUMBER* ;
Date : Name ;
Expr : Expression (Felan)? ;
Felan : Expr Operands Expr (Felan)?;
Expression : Int | Double | Date
		   | LPAREN Expr RPAREN
		   | Funccall ;
Args : Arg ( COMMA Arg)* ;
Arg : Expr ;
Functions : (AND | OR | THEN | SCALAX | SCALA | TRUNCATE);
Funccall : Name LPAREN Args RPAREN
		 | MKDATE LPAREN Arg COMMA Arg RPAREN
		 | Functions LPAREN Arg COMMA Arg RPAREN
		 | ONE LPAREN RPAREN
		 | GIVE LPAREN Arg RPAREN ;