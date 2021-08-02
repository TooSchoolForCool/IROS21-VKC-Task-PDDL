(define (domain picknplace)
    (:requirements :typing :strips :equality)
    (:types  
        loc_base loc_object - location
        block - object
        base arm - robot)
    (:constants robhand - arm)
    (:predicates 
        (at_base ?lb - loc_base)
		(at_object ?b - block ?lo - loc_object)
		(free ?a - arm)
		(carry ?b - block ?a - arm)
		(reachable ?lo - loc_object ?lb - loc_base)
		(occupied ?lo - loc_object)
    )
   
    (:action pick
        :parameters (
            ?obj - block 
            ?lo - loc_object 
            ?arm - arm 
            ?lb - loc_base
        )
        :precondition (and
            (at_object ?obj ?lo) 
            (at_base ?lb)
            (reachable ?lo ?lb) 
            (free ?arm))
        :effect (and 
            (carry ?obj ?arm)
		    (not (at_object ?obj ?lo)) 
		    (not (free ?arm))
		    (not (occupied ?lo))
		)
    )
   (:action move
       :parameters  (?from ?to - loc_base)
       :precondition (at_base ?from)
       :effect (and  (at_base ?to)
                    (not (at_base ?from))))
   (:action place
       :parameters  (?obj - block ?lo - loc_object ?arm - arm ?lb - loc_base)
       :precondition  (and  (carry ?obj ?arm) 
                            (at_base ?lb)
                            (reachable ?lo ?lb)
                            (not (occupied ?lo))
                            )
       :effect (and (not (carry ?obj ?arm))
		            (at_object ?obj ?lo)
		            (free ?arm)
		            (occupied ?lo)
		            ))
)
