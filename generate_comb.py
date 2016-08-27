import sys
import pprint

# 4人の中からペアを組むすべての組み合わせをリストで返す
# 引数：4桁の整数
# 戻り値：リスト
def createPair(member):
  member_list = list(member)
  result_list = []
  tmp_list = []
  for i in range(0, len(member_list)-1):
    for j in range(i+1, len(member_list)):
      # listのコピーを作成
      tmp_list[:] = member_list
      two_pair = "";
      # 1組を決定する
      two_pair += tmp_list[i]+tmp_list[j]
      # 残りの要素2つがもう一組
      del tmp_list[j]
      del tmp_list[i]
      for item in tmp_list:
        two_pair += item
      result_list.append(two_pair)
  return result_list

# N人から4人抜き出す
# 引数：整数N
# 戻り値：4桁の整数
def selectFourCharacters(count):
  return count

# memberにある値に対応する要素をインクリメントする
# 引数1：各メンバーの選択された回数を保持するリスト
# 引数2：選択された4人(文字列)
def coutUpList(used_list, member):
  return memberList

# memberに対応するpairHash内のリストの要素を削除
# 引数１：メンバーの組み合わせを保持するHash
# 引数2：選択された4人(文字列)
def removeListOnHash(pair_hash, member):
  return pairHash

# pair_hashにあるpairを列挙していく
# used_list内で選択された数が少ない人から選択する
# 一度出力したpairは削除
# hash内のリストが全てからになったら終了
def printPairs(pair_hash, used_list):
  return pair_hash

if __name__ == '__main__':
  member_count = int(sys.argv[1])
  # comb_pair["4人のペア"] = list(comb1,comb2,...)
  comb_pair = {}

  # str_num = "123"
  # num = int(str_num)
  # それぞれのメンバーの選択された回数を保存しておく
  used_list = [0] * member_count
  print (len(used_list))
  print(createPair("1234"))

