import io
with open(r'd:\Phase2_Xbrain\fintech\budgetbot\docs\slides\presentation.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx1 = -1
end_idx1 = -1
for i, line in enumerate(lines):
    if '<!-- 15 · THE NUMBERS (THÀNH QUẢ) -->' in line:
        start_idx1 = i
    if '<!-- 17 · TRANSITION TO AI (NEW SLIDE) -->' in line:
        end_idx1 = i

insert_idx = -1
for i, line in enumerate(lines):
    if '<!-- 21 · LESSON 1 -->' in line:
        insert_idx = i

if start_idx1 != -1 and end_idx1 != -1 and insert_idx != -1:
    chunk_to_move = lines[start_idx1:end_idx1]
    del lines[start_idx1:end_idx1]
    new_insert_idx = insert_idx - (end_idx1 - start_idx1)
    lines[new_insert_idx:new_insert_idx] = chunk_to_move
    with open(r'd:\Phase2_Xbrain\fintech\budgetbot\docs\slides\presentation.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print('Done')
else:
    print('Failed to find boundaries')
