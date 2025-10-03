class Message {
  const Message({
    required this.id,
    required this.chatId,
    required this.senderId,
    required this.text,
    required this.sentAtIso,
    this.isRead = false,
  });

  final String id;
  final String chatId;
  final String senderId;
  final String text;
  final String sentAtIso;
  final bool isRead;
}
