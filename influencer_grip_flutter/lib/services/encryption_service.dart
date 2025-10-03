import 'dart:convert';
import 'dart:math';
import 'package:encrypt/encrypt.dart';
import '../models/encryption_settings.dart';

class EncryptionService {
  final EncryptionSettings _settings = const EncryptionSettings();

  EncryptionSettings get settings => _settings;

  String encrypt(String plaintext, String key) {
    try {
      final keyBytes = _generateKeyFromString(key);
      final iv = IV.fromSecureRandom(16);

      final encrypter = Encrypter(AES(keyBytes));

      final encrypted = encrypter.encrypt(plaintext, iv: iv);

      // Return encrypted data with IV for decryption
      return '${iv.base64}:${encrypted.base64}';
    } catch (e) {
      throw Exception('Encryption failed: $e');
    }
  }

  String decrypt(String encryptedData, String key) {
    try {
      final parts = encryptedData.split(':');
      if (parts.length != 2) {
        throw Exception('Invalid encrypted data format');
      }

      final iv = IV.fromBase64(parts[0]);
      final encryptedText = parts[1];

      final keyBytes = _generateKeyFromString(key);
      final encrypter = Encrypter(AES(keyBytes));

      return encrypter.decrypt64(encryptedText, iv: iv);
    } catch (e) {
      throw Exception('Decryption failed: $e');
    }
  }

  Key _generateKeyFromString(String keyString) {
    final keyBytes = utf8.encode(keyString);
    final hash = sha256.convert(keyBytes);

    // Use first 32 bytes for AES-256
    return Key(hash.bytes.sublist(0, 32));
  }

  String generateRandomKey({int length = 32}) {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    final random = Random.secure();

    return List.generate(length, (index) {
      return chars[random.nextInt(chars.length)];
    }).join();
  }

  bool isValidKey(String key) {
    return key.length >= 16; // Minimum key length for security
  }
}