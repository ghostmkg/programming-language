fn bubble_sort(arr: &mut [i32]) {
    let len = arr.len();
    for i in 0..len {
        for j in 0..len - i - 1 {
            if arr[j] > arr[j + 1] {
                arr.swap(j, j + 1); // Swap elements if they’re out of order
            }
        }
    }
}

fn main() {
    let mut numbers = [64, 34, 25, 12, 22, 11, 90];
    println!("Original array: {:?}", numbers);
    
    bubble_sort(&mut numbers);
    println!("Sorted array: {:?}", numbers);
}
