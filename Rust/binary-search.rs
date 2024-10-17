fn binary_search(arr: &[i32], target: i32) -> Option<usize> {
    let mut low = 0;
    let mut high = arr.len() as i32 - 1;

    while low <= high {
        let mid = low + (high - low) / 2;
        let mid_value = arr[mid as usize];

        if mid_value == target {
            return Some(mid as usize);
        } else if mid_value < target {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    None
}

fn main() {
    let sorted_array = [1, 3, 5, 7, 9, 11, 13, 15];
    let target = 7;

    match binary_search(&sorted_array, target) {
        Some(index) => println!("Found target {} at index {}.", target, index),
        None => println!("Target {} not found in array.", target),
    }
}
