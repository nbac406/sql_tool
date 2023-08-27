from tkinter import *
from tkinter import ttk
import pymysql

# pymysql 설정
conn = pymysql.connect(
    host="127.0.0.1",
    user="????",
    password="????",
    database="????"
)
cur = conn.cursor()

def call_procedure(input_name_entry, tree, procedure_name):
    input_name = input_name_entry.get()
    cur.callproc(procedure_name, (input_name,))
    results = cur.fetchall()

    # 조회 결과를 Treeview에 표시
    tree.delete(*tree.get_children())  # 기존 데이터 삭제
    if len(results) > 0:  # 결과가 있을 경우
        for row in results:
            tree.insert("", "end", values=row)
    else:
        tree.insert("", "end", values=("조회 결과 없음",))  # 결과 없음 메시지 추가

def open_search_window(procedure_name, window_title, columns, label_text): 
    search_window = Toplevel(root)
    search_window.title(window_title)
    search_window.geometry("1500x900")  
    
    input_name_label = Label(search_window, text=label_text + ":")
    input_name_label.pack()
    input_name_entry = Entry(search_window)
    input_name_entry.pack()
    
    call_search_button = Button(search_window, text="검색", command=lambda: call_procedure(input_name_entry, tree, procedure_name))
    call_search_button.pack()

    tree = ttk.Treeview(search_window, columns=[col[0] for col in columns], show="headings")
    for col, width in columns:
        tree.column(col, width=width)
        tree.heading(col, text=col)

    tree.pack()

root = Tk()
root.title("Project Tool")
root.geometry("600x400")

start_frame = Frame(root)
start_frame.pack()

welcome_label = Label(start_frame, text="플레이어 정보 검색 도구")
welcome_label.pack()
search_button = Button(start_frame, text="플레이어 정보", command=lambda: open_search_window("GetPlayerInfo", "플레이어 조회", [
        ("NUM", 100),
        ("match_id", 100),
        ("player_name", 100),
        ("account_id", 100),
        ("roster_id", 100),
        ("team_ranking", 100),
        ("dbnos", 100),
        ("assists", 100),
        ("damage_dealt", 100),
        ("headshot_kills", 100),
        ("kills", 100),
        ("longest_kill", 100),
        ("team_kills", 100),
        ("ride_distance", 100),
        ("swim_distance", 100),
        ("walk_distance", 100),
        ("players_table_id", 100)
    ], label_text="플레이어 이름"))
search_button.pack()

weapon_search_button = Button(start_frame, text="플레이어 무기정보", command=lambda: open_search_window("GetPlayerWeaponInfo", "플레이어 무기 정보 조회", [
        ("player_name", 100),
        ("account_id", 100),
        ("first_weapon_name", 100),
        ("first_weapon_XPtotal", 100),
        ("second_weapon_name", 100),
        ("second_weapon_XPtotal", 100),
        ("third_weapon_name", 100),
        ("third_weapon_XPtotal", 100),
        ("weapon_cluster", 100)
    ], label_text="플레이어 이름"))
weapon_search_button.pack()

distance_search_button = Button(start_frame, text="플레이어 이동정보", command=lambda: open_search_window("GetPlayerDistance", "플레이어 이동 정보 조회", [
        ("match_id", 100),
        ("victim_name", 100),
        ("killer_x", 100),
        ("killer_y", 100)
    ], label_text="플레이어 이름"))
distance_search_button.pack()

attacker_damagereason_button = Button(start_frame, text="사격부위", command=lambda: open_search_window("GetAttackersByDamageReason", "플레이어 사격 정보 조회", [
        ("attacker_name", 100),
        ("attacker_damagereason", 150),
        ("total_damage", 100)
    ], label_text="사격부위"))
attacker_damagereason_button.pack()


root.mainloop()
