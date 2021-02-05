#-*- coding:utf-8 -*-
import os
import numpy as np
import pandas as pd
import pickle


def set_landmark():
    """
    初期ランドマーク名設定ファイルの作成
    """
    Erangel = ["1:Zharki", "2:Shooting Range", "3:Severny", "4:Stalber",
                "5:Kameshki", "6:North Georgopol", "7:South Georgopol", "8:Contena",
                "9:Yasnaya Polyana", "10:Rozhok", "11:Hospital", "12:Ruins(Era)", "13:School",
                "14:Mansion", "15:Lipovka", "16:Prison(Era)", "17:Gatka", "18:Pochinki",
                "19:Shelter", "20:Farm", "21:Mylta", "22:Mylta Power", "23:Quarry(Era)",
                "24:Ferry Pier", "25:Primorsk", "26:Sosnovka Military Base",
                "27:Novorepnoye", "28:Atlantis", "29:Twelve Castella Houses", "30:West Coast",
                "31:Chopsticks", "32:Fairy Forest"]

    Miramar = ["1:Ruins(Mir)", "2:Trailer Park", "3:La Cobreria", "4:Torre Ahumada",
                "5:Campo Militar", "6:Tierra Bronca", "7:Cruz del Valle",
                "8:Crater Fields", "9:El Pozo", "10:Water Treatment", "11:El Azahar",
                "12:Hacienda del Patron", "13:San Martin", "14:Junkyard",
                "15:Minas Generales", "16:Graveyard", "17:Power Grid", "18:Pecado",
                "19:Monte Nuevo", "20:La Bendita", "21:Ladrillera", "22:Chumacera",
                "23:Los Leones", "24:Impara", "25:Minas del Valle", "26:Valle del Mar",
                "27:Minas del Sur", "28:Prison(Mir)", "29:Los Higos", "30:Puerto Paraiso",
                "31:Oasis", "32:South Coast"]

    Sanhok = ["1:Ha Tinh", "2:Khao", "3:Mongnai", "4:Tat Mok", "5:Paradise Resort",
                "6:Camp Alpha", "7:Bootcamp", "8:Bhan", "9:Camp Bravo",
                "10:Ruins(San)", "11:Pai Nan", "12:Quarry(San)", "13:Lakawi",
                "14:Kampong", "15:Cave", "16:Docks", "17:Camp Charlie", "18:Tambang",
                "19:Na Kham", "20:Sahmee", "21:Ban Tai", "22:Horse", "23:Northwest Riverside",
                "24:Northwest Summit", "25:Village on the cliff"]

    Vikendi = ["1:Port", "2:Zabava", "3:Trevno", "4:Coal Mine", "5:Cosmodrome",
                "6:Krichas", "7:Dobro Mesto", "8:Goroka", "9:Mount Kreznic",
                "10:Podvosto", "11:Peshkova", "12:Villa", "13:Movatra", "14:Vihar",
                "15:Dino Park", "16:Abbey", "17:Castle", "18:Cement Factory",
                "19:Tovar", "20:Lumber Yard", "21:Volnova", "22:Hot Springs",
                "23:Cantra", "24:Winery", "25:Milnar", "26:Sawmill", "27:Pilnec",
                "28:Hidden Cave", "29:Ponds", "30:North Bridge", "31:East Coast",
                "32:Villa Forest", "33:GCZ Intersection"]

    with open('./Erangel.txt', 'wb') as f:
        pickle.dump(Erangel, f)
    with open('./Miramar.txt', 'wb') as f:
        pickle.dump(Miramar, f)
    with open('./Sanhok.txt', 'wb') as f:
        pickle.dump(Sanhok, f)
    with open('./Vikendi.txt', 'wb') as f:
        pickle.dump(Vikendi, f)


def is_int(s):
    """
    標準入力された文字列が数値かどうか判定
    """
    try:
        int(s)

        return True
    except ValueError:

        return False


def make_new_file():
    name = input("最初に入力するチーム名を入力してください(終了したい場合は2)：")
    if is_int(name) == True and int(name) == 2:
        print("終了します")
        exit(1)

    Erangel, Miramar, Sanhok, Vikendi = get_landmark_name()

    new_data = [[0 for i in range(len(Erangel + Miramar + Sanhok + Vikendi))]]
    new_data = pd.DataFrame(new_data, columns = Erangel + Miramar + Sanhok + Vikendi, index = [name])
    landmark_data = rewrite(new_data.shape[0] - 1, new_data)
    landmark_data.to_csv("./landmark.csv", header = True, index = True, encoding = 'utf_8_sig')


def rewrite(team_num, landmark_data):
    """
    各ランドマークへの降下回数を更新
    """
    Erangel, Miramar, Sanhok, Vikendi = get_landmark_name()

    matches = int(input("何試合分入力しますか？(半角数字のみ入力)："))
    for match in range(matches):
        map = input("マップ名を数字で選択してください(1:Erangel, 2:Miramar, 3:Sanhok, 4:Vikendi, 5:終了)：")
        while(is_int(map) != True or int(map) not in [1, 2, 3, 4, 5]):
            map = input("日本語読めねえのかカス(もう一度お願いします)：")

        if int(map) == 5:
            print("書き換えずに終了します")
            exit(1)

        if int(map) == 1:
            for era_mark in Erangel:
                print(era_mark)
            column = 0
        elif int(map) == 2:
            for mir_mark in Miramar:
                print(mir_mark)
            column = len(Erangel)
        elif int(map) == 3:
            for san_mark in Sanhok:
                print(san_mark)
            column = len(Erangel + Miramar)
        elif int(map) == 4:
            for vik_mark in Vikendi:
                print(vik_mark)
            column = len(Erangel + Miramar + Sanhok)
        mark = input("該当するランドマークの数字を選んで下さい：")

        try:
            mark = int(mark)
        except InputError:
            print("丁寧なエラー処理書くのめんどくなったからやり直してね")

        landmark_data.iat[team_num, column + mark - 1] += 1

    return landmark_data


def add_new_team(name, landmark_data):
    """
    新規チームの登録
    """
    Erangel, Miramar, Sanhok, Vikendi = get_landmark_name()

    new_data = [[0 for i in range(len(Erangel + Miramar + Sanhok + Vikendi))]]
    new_data = pd.DataFrame(new_data, columns=Erangel + Miramar + Sanhok + Vikendi, index=[name])
    landmark_data = pd.concat([landmark_data, new_data], sort=False)
    landmark_data = rewrite(landmark_data.shape[0]-1, landmark_data)

    return landmark_data


def update_landmark_data(name):
    """
    update landmark.csv
    """
    flag = False
    landmark_data = pd.read_csv("./landmark.csv", delimiter=",", index_col=0)
    index = list(landmark_data.index)

    for team in range(landmark_data.shape[0]):
        if name == index[team]:
            flag = True
            print("チームが見つかりました：", index[team])
            ans = input("このチームのデータを書き換えますか？(はい：0, いいえ：1)：")
            while(is_int(ans) != True or int(ans) not in [0, 1]):
                ans = input("日本語読めねえのかカス(もう一度お願いします)：")
            if int(ans) == 1:
                print("終了します")
                exit(1)
            elif int(ans) == 0:
                landmark_data = rewrite(team, landmark_data)  # データの書き換え

    if flag != True:
        print("チームが見つかりませんでした")
        num = input("新規チームとして登録しますか？(はい：0, いいえ：1)：")
        while(is_int(num) != True or int(num) not in [0, 1]):
            num = input("日本語読めねえのかカス(もう一度お願いします)：")
        if int(num) == 1:
            print("終了します")
            exit(1)
        elif int(num) == 0:
            landmark_data = add_new_team(name, landmark_data)  # 新規チームとして登録

    ans = input("今回の変更を保存してよろしいですか？(はい：0, いいえ：1)：")
    while(is_int(ans) != True or int(ans) not in [0, 1]):
        ans = input("日本語読めねえのかカス(もう一度お願いします)：")

    if int(ans) == 1:
        print("変更せずに終了しました")
        exit(1)
    elif int(ans) == 0:
        landmark_data.to_csv("./landmark.csv", header=True, index=True, encoding='utf_8_sig')
        print("変更を保存しました")


def landmark_input():
    """
    save landmark as csv
    """
    if os.path.isfile("./landmark.csv") != True:
        print("過去のデータが見つからないため, 新しくランドマークファイルを生成します")
        make_new_file()

    team_name = input("次のチーム名を入力してください(終了したい場合は2)：")
    if is_int(team_name) == True and int(team_name) == 2:
        print("終了します")
        exit(1)

    else:
        update_landmark_data(team_name)


def get_landmark_name():
    """
    ランドマーク一覧を取得
    """
    with open("./Erangel.txt", "rb") as f:
        Erangel = pickle.load(f)
    with open("./Miramar.txt", "rb") as f:
        Miramar = pickle.load(f)
    with open("./Sanhok.txt", "rb") as f:
        Sanhok = pickle.load(f)
    with open("./Vikendi.txt", "rb") as f:
        Vikendi = pickle.load(f)

    return Erangel, Miramar, Sanhok, Vikendi


def search_landmark(n_landmarks=3):
    """
    入力されたチームの各マップで最も降下回数の多い場所を表示
    """
    Erangel, Miramar, Sanhok, Vikendi = get_landmark_name()

    maps = ["Erangel", "Miramar", "Sanhok", "Vikendi"]
    if os.path.isfile("./landmark.csv") != True:
        print("データが存在しません")
        exit(1)

    landmark_data = pd.read_csv("./landmark.csv", delimiter=",", index_col=0)
    index = list(landmark_data.index)
    column = list(landmark_data.columns)
    name = input("チーム名を入力してください：")

    flag = False
    for team in range(landmark_data.shape[0]):
        if name == index[team]:
            flag = True
            print("チームが見つかりました")
            print(index[team])
            era = landmark_data.iloc[team, :len(Erangel)]
            era = era.sort_values(ascending=False)
            mir = landmark_data.iloc[team, len(Erangel):len(Erangel)+len(Miramar)]
            mir = mir.sort_values(ascending=False)
            san = landmark_data.iloc[team, len(Erangel)+len(Miramar):len(Erangel)+len(Miramar)+len(Sanhok)]
            san = san.sort_values(ascending=False)
            vik = landmark_data.iloc[team, len(Erangel)+len(Miramar)+len(Sanhok):]
            vik = vik.sort_values(ascending=False)

            print("Erangel")
            for i in range(n_landmarks):
                print("  {0} (降下回数{1}/{2})".format(era.index[i], era[i], era.sum()))
            print("Miramar")
            for i in range(n_landmarks):
                print("  {0} (降下回数{1}/{2})".format(mir.index[i], mir[i], mir.sum()))
            print("Sanhok")
            for i in range(n_landmarks):
                print("  {0} (降下回数{1}/{2})".format(san.index[i], san[i], san.sum()))
            print("Vikendi")
            for i in range(n_landmarks):
                print("  {0} (降下回数{1}/{2})".format(vik.index[i], vik[i], vik.sum()))

            break

    if not flag:
        print("入力されたチームは見つかりませんでした")


def rename_team():
    """
    チーム名の変更
    """
    if os.path.isfile("./landmark.csv") != True:
        print("データが存在しません")
        exit(1)

    landmark_data = pd.read_csv("./landmark.csv", delimiter=",", index_col=0)
    index = list(landmark_data.index)
    org_name = input("変更元のチーム名を入力してください：")

    flag = False
    for team in range(landmark_data.shape[0]):
        if org_name == index[team]:
            flag = True
            new_name = input("新しいチーム名を入力してください：")
            renamed_landmark_data = landmark_data.rename(index={org_name: new_name})
            renamed_landmark_data.to_csv("./landmark.csv", header=True, index=True, encoding='utf_8_sig')
            print("変更を保存しました")
            break

    if not flag:
        print("入力されたチームは見つかりませんでした")


def add_new_landmark():
    """
    新しい地名を追加
    """
    if os.path.isfile("./landmark.csv") != True:
        print("元となるデータが存在しません")
        exit(1)

    Erangel, Miramar, Sanhok, Vikendi = get_landmark_name()

    map = input("マップ名を数字で選択してください(1:Erangel, 2:Miramar, 3:Sanhok, 4:Vikendi, 5:終了)：")
    while(is_int(map) != True or int(map) not in [1, 2, 3, 4, 5]):
        map = input("日本語読めねえのかカス(もう一度お願いします)：")

    if int(map) != 5:
        new_landmark = input("新しく利用したいランドマーク名を入力してください：")
        file = pd.read_csv("./landmark.csv", delimiter=",", index_col=0)

    if int(map) == 5:
        print("書き換えずに終了します")

    elif int(map) == 1:
        file.insert(len(Erangel), "{0}:{1}".format(len(Erangel)+1, new_landmark), 0)
        Erangel.append("{0}:{1}".format(len(Erangel)+1, new_landmark))
        with open('./Erangel.txt', 'wb') as f:
            pickle.dump(Erangel, f)

    elif int(map) == 2:
        file.insert(len(Erangel+Miramar), "{0}:{1}".format(len(Miramar)+1, new_landmark), 0)
        Miramar.append("{0}:{1}".format(len(Miramar)+1, new_landmark))
        with open('./Miramar.txt', 'wb') as f:
            pickle.dump(Miramar, f)

    elif int(map) == 3:
        file.insert(len(Erangel+Miramar+Sanhok), "{0}:{1}".format(len(Sanhok)+1, new_landmark), 0)
        Sanhok.append("{0}:{1}".format(len(Sanhok)+1, new_landmark))
        with open('./Sanhok.txt', 'wb') as f:
            pickle.dump(Sanhok, f)

    elif int(map) == 4:
        file.insert(len(Erangel+Miramar+Sanhok+Vikendi), "{0}:{1}".format(len(Vikendi)+1, new_landmark), 0)
        Vikendi.append("{0}:{1}".format(len(Vikendi)+1, new_landmark))
        with open('./Vikendi.txt', 'wb') as f:
            pickle.dump(Vikendi, f)

    if int(map) != 5:
        file.to_csv("./landmark.csv", header=True, index=True, encoding='utf_8_sig')


def fix_data():
    """
    登録した情報の修正
    """
    num = input("(チーム名の変更：0, 地名の登録：1, 終了：2)：")
    while(is_int(num) != True or int(num) not in [0, 1, 2]):
        num = input("日本語読めねえのかカス(もう一度お願いします)：")

    if int(num) == 2:
        print("終了します")

    elif int(num) == 0:
        rename_team()

    elif int(num) == 1:
        add_new_landmark()


def main():
    # ランドマーク設定ファイルが存在するか確認
    if not os.path.isfile("./Erangel.txt") or not os.path.isfile("./Miramar.txt") or not os.path.isfile("./Sanhok.txt") or not os.path.isfile("./Vikendi.txt"):
        print("ランドマーク名設定ファイルが見つかりません")
        set_landmark()
        print("ランドマーク名設定ファイルを作成しました")

    while(True):
        # モードの選択
        num = input("半角数字を入力してください(登録：0, 検索：1, 修正：2, 終了：3)：")
        while(is_int(num) != True or int(num) not in [0, 1, 2, 3]):
            num = input("日本語読めねえのかカス(もう一度お願いします)：")

        if int(num) == 3:
            print("終了します")
            exit(1)
        elif int(num) == 0:
            print("登録モード")
            landmark_input()
        elif int(num) == 1:
            print("検索モード")
            search_landmark()
        elif int(num) == 2:
            print("修正モード")
            fix_data()

        print("\n")


if __name__ == "__main__":
    main()
