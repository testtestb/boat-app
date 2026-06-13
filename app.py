import SwiftUI
import PhotosUI

struct CameraView: View {
    @State private var showingImagePicker = false
    @State private var inputImage: UIImage?

    var body: some View {
        VStack {
            Button("カメラを起動") {
                self.showingImagePicker = true
            }
        }
        .sheet(isPresented: $showingImagePicker) {
            ImagePicker(image: $inputImage)
        }
        .onChange(of: inputImage) { _ in
            saveImageToLibrary()
        }
    }

    // 写真をライブラリに保存する関数
    func saveImageToLibrary() {
        guard let inputImage = inputImage else { return }
        UIImageWriteToSavedPhotosAlbum(inputImage, nil, nil, nil)
    }
}
