(define (domain picknplace)
    (:requirements :typing :strips :equality)
    (:types  
        loc_base loc_object - location
        block - object
        base arm vkc - robot)
    (:constants robhand - vkc)
    (:predicates 
        (at_base ?lb - loc_base)
		(at_object ?b - block ?lo - loc_object)
		(free ?a - vkc)
		(carry ?b - block ?a - vkc)
		(occupied ?lo - loc_object)
    )
   
    (:action pick_vkc
        :parameters (
            ?obj - block 
            ?lo - loc_object
            ?arm - vkc)
        :precondition (and
            (at_object ?obj ?lo) 
            (free ?arm)
        )
        :effect (and
            (carry ?obj ?arm)
		    (not (at_object ?obj ?lo)) 
		    (not (free ?arm))
		    (not (occupied ?lo))
		)
    )
    (:action place_vkc
       :parameters  (?obj - block ?lo - loc_object ?arm - vkc)
       :precondition  (and  (carry ?obj ?arm) 
                            (not (occupied ?lo))
                            )
       :effect (and (not (carry ?obj ?arm))
		            (at_object ?obj ?lo)
		            (free ?arm)
		            (occupied ?lo)
		            ))
   
)
