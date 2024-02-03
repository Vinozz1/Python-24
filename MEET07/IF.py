print( "<<\t\t NILAI AKHIR SEMESTER \t\t>>" )

pts = int ( input( "Masukan nilai PTS :" ) )
pas = int ( input( "Masukan nilai PAS :" ) )

nilai_akhir = (0.40 * pts) + (0.60 * pas)

print( f"Nilai akhir = {nilai_akhir}" )
if nilai_akhir == 100:
    print ( "<<< Sempurna >>>" )
else:
    print ( "<<< Skill Issue >>>" )