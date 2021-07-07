/* In JS */

function merge_sort(first, second) {
  var merged_list = [];
  var length = first.length + second.length;
  var j = 0;
  var k = 0;
  for (var i = 0; i < length; i++) {
    if (first[j] < second[k] || second[k] == undefined) {
      merged_list.push(first[j]);
      j++;
    } else {
      merged_list.push(second[k]);
      k++;
    }
  }
  return merged_list;
}