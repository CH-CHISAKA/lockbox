# InfluencerGrip Flutter App

A secure messaging application built with Flutter and Dart, featuring end-to-end encryption, SMS OTP verification, and network device discovery.

## Features

- **🔐 End-to-end encryption** with AES-256
- **📱 SMS OTP verification** for secure authentication
- **🌐 Network device discovery** for peer-to-peer communication
- **⚡ Real-time messaging** with encryption/decryption
- **🎨 Modern UI** with dark theme and gradient backgrounds
- **📱 Cross-platform** support (iOS and Android)

## Architecture

This application follows the **MVC (Model-View-Controller)** architecture pattern:

### Models
- `Message` - Represents encrypted/decrypted messages
- `NetworkDevice` - Handles device discovery and management
- `EncryptionSettings` - Configuration for encryption algorithms

### Views
- `MainScreen` - Main application interface
- `Sidebar` - Navigation and server controls
- `HomeView` - Welcome screen with device status
- `SendMessageView` - Message encryption interface
- `ReceiveMessageView` - Message decryption interface
- `AboutView` - Application information

### Controllers
- `AppController` - Main application state management
- Business logic coordination between services

### Services
- `EncryptionService` - AES encryption/decryption operations
- `NetworkService` - Device discovery and server management
- `SmsService` - OTP generation and verification

## Getting Started

### Prerequisites

- Flutter SDK (3.0.0 or higher)
- Dart SDK (2.19.0 or higher)
- Android Studio (for Android development)
- Xcode (for iOS development)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd influencer_grip_flutter
```

2. Install dependencies:
```bash
flutter pub get
```

3. Run the application:
```bash
# For Android
flutter run -d android

# For iOS
flutter run -d ios

# For web (if supported)
flutter run -d web
```

## Usage

### Starting the Server

1. Open the app and click "Start Server" in the sidebar
2. The server will start on port 8080
3. The indicator will turn green when the server is running

### Sending Encrypted Messages

1. Navigate to "Send Message" tab
2. Enter your message in the text field
3. Provide an encryption key (minimum 16 characters)
4. Click "Encrypt Message" to encrypt your message
5. The encrypted message will be displayed and can be copied

### Receiving and Decrypting Messages

1. Navigate to "Receive Message" tab
2. Paste the encrypted message
3. Enter the same encryption key used for encryption
4. Click "Decrypt Message" to reveal the original message

### SMS OTP Verification

The app includes SMS OTP functionality for secure authentication:

1. Enter a phone number for OTP verification
2. The app will send a 6-digit code via SMS
3. Enter the received code to verify

## Security Features

- **AES-256 Encryption**: Industry-standard encryption algorithm
- **Secure Key Management**: Keys are processed locally and never stored
- **OTP Authentication**: SMS-based verification for secure access
- **Network Security**: Encrypted communication between devices

## Dependencies

Key packages used in this project:

- `provider`: State management
- `encrypt`: AES encryption algorithms
- `sms_advanced`: SMS functionality
- `connectivity_plus`: Network connectivity checks
- `permission_handler`: Runtime permissions
- `qr_flutter`: QR code generation for sharing keys

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions, please open an issue in the GitHub repository.

---

Built with ❤️ using Flutter and Dart