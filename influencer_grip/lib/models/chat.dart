class Chat {
  const Chat({
    required this.id,
    required this.participantIds,
    required this.lastMessage,
  });

  final String id;
  final List<String> participantIds; // includes current user id
  final String lastMessage;
}
