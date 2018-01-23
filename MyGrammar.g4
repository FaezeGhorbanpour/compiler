grammar MyGrammar;




// Parser Rules

program : (assign | funcall | method )+ ;
lowercasenumber : (LOWERCASE | NUMBER);
name : LOWERCASE lowercasenumber*;
method : name ASSIGNMENT (defvar | deffunc)
	 | TIMEFUNCT LPAREN deffunc RPAREN ;
funcall : name LPAREN args RPAREN
		 | MKDATE LPAREN arg COMMA arg RPAREN
		 | functions LPAREN arg COMMA arg RPAREN
		 | ONE LPAREN RPAREN
		 | GIVE LPAREN arg RPAREN ;
assign : name EQUAL  expr ;
kind : (INT | DOUBLE  | DATE | CONTRACT);
operands : (PLUS | MINUS | DIV | TIMES) ;
deffunc : LPAREN kind (COMMA kind)*  RPAREN TO kind ;
defvar : kind ;
integer : name
	|  NUMBER+ ;
doub : name
	   | NUMBER+ DOT NUMBER* ;
dat : name ;
expr : expression (felan)? ;
felan : expr operands expr (felan)?;
expression : integer | doub | dat
		   | LPAREN expr RPAREN
		   | funcall ;
args : arg ( COMMA arg)* ;
arg : expr ;
functions : (AND | OR | THEN | SCALAX | SCALA | TRUNCATE);



// Lexer Rules

DOUBLE : 'Double' ;
INT : 'Int' ;
DATE : 'Date';
CONTRACT : 'Contract' ;
PLUS : '+' ;
MINUS : '-' ;
TIMES : '*' ;
DIV : '/';
AND : 'and' ;
OR : 'or' ;
THEN : 'then' ;
SCALAX : 'scalaX' ;
SCALA : 'scale' ;
TRUNCATE : 'truncate' ;
TO : '->';
ASSIGNMENT : '::';
LPAREN : '(' ;
RPAREN : ')' ;
ONE : 'one' ;
COMMA : ',' ;
DOT : '.' ;
EQUAL : '=' ;
TIMEFUNCT : 'TimeFunc' ;
MKDATE : 'mkDate' ;
GIVE : 'give' ;
//WS : [ \t\r\n]+ -> skip ;
WS : (' ' | '\t' | '\r'| '\n')  -> skip ;
NUMBER : ('0'..'9') ;
LOWERCASE : ('a'..'z');
//lowercasenumber : ('0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'  | 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' );
//NUMBER :( '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' );
//LOWERCASE :( 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' );