# P_D = 0.01
# P_Pos_D = 0.99
# P_Pos_NotD = 0.05
# P_NotD = 1 - P_D

# P_D_Pos = (P_Pos_D * P_D) / ((P_Pos_D * P_D) + (P_Pos_NotD * P_NotD))

# print("Probability that person actually has disease:")
# print(round(P_D_Pos * 100, 2), "%")
















ch_des = 0.01
ch_no_des = 0.99
ch_false_rep = 0.05
ch_total_normal = 1-ch_des

prob = (ch_des*ch_no_des)/((ch_des*ch_no_des)+(ch_false_rep*ch_total_normal))

print("probability of ------------")

main_prob = round(prob*100,2)

print("ans is ", main_prob ,"%")



