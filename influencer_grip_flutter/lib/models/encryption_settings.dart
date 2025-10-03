class EncryptionSettings {
  final String algorithm;
  final int keySize;
  final String mode;

  const EncryptionSettings({
    this.algorithm = 'AES',
    this.keySize = 256,
    this.mode = 'CBC',
  });

  factory EncryptionSettings.fromJson(Map<String, dynamic> json) {
    return EncryptionSettings(
      algorithm: json['algorithm'] ?? 'AES',
      keySize: json['keySize'] ?? 256,
      mode: json['mode'] ?? 'CBC',
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'algorithm': algorithm,
      'keySize': keySize,
      'mode': mode,
    };
  }
}

class ServerSettings {
  final int port;
  final bool autoStart;
  final int maxConnections;

  const ServerSettings({
    this.port = 8080,
    this.autoStart = false,
    this.maxConnections = 10,
  });

  factory ServerSettings.fromJson(Map<String, dynamic> json) {
    return ServerSettings(
      port: json['port'] ?? 8080,
      autoStart: json['autoStart'] ?? false,
      maxConnections: json['maxConnections'] ?? 10,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'port': port,
      'autoStart': autoStart,
      'maxConnections': maxConnections,
    };
  }
}