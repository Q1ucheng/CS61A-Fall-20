(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)


(define (sign num)
  (cond
    ((< num 0) -1)
    ((= num 0) 0)
    (else 1)
  )
)


(define (square x) (* x x))

(define (pow x y)
  (cond 
    ((= y 0) 1)
    ((= y 1) x)
    ((odd? y) (* x (pow x (- y 1))))
    (else (pow (square x) (/ y 2)))
  )
)

