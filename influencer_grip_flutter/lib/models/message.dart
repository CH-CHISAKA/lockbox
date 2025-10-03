class Message {
  final String id;
  final String content;
  final String senderId;
  final String receiverId;
  final DateTime timestamp;
  final bool isEncrypted;
  final MessageType type;

  Message({
    required this.id,
    required this.content,
    required this.senderId,
    required this.receiverId,
    required this.timestamp,
    required this.isEncrypted,
    required this.type,
  });

  factory Message.fromJson(Map<String, dynamic> json) {
    return Message(
      id: json['id'],
      content: json['content'],
      senderId: json['senderId'],
      receiverId: json['receiverId'],
      timestamp: DateTime.parse(json['timestamp']),
      isEncrypted: json['isEncrypted'],
      type: MessageType.values[json['type']],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'content': content,
      'senderId': senderId,
      'receiverId': receiverId,
      'timestamp': timestamp.toIso8601String(),
      'isEncrypted': isEncrypted,
      'type': type.index,
    };
  }
}

enum MessageType {
  text,
  image,
  file,
  otp,
}

class EncryptedMessage {
  final String encryptedContent;
  final String iv;
  final String key;

  EncryptedMessage({
    required this.encryptedContent,
    required this.iv,
    required this.key,
  });

  factory EncryptedMessage.fromJson(Map<String, dynamic> json) {
    return EncryptedMessage(
      encryptedContent: json['encryptedContent'],
      iv: json['iv'],
      key: json['key'],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'encryptedContent': encryptedContent,
      'iv': iv,
      'key': key,
    };
  }
}