import 'package:flutter/material.dart';
import '../../models/chat.dart';
import 'avatar.dart';

class ChatListItem extends StatelessWidget {
  const ChatListItem({super.key, required this.chat, this.onTap});
  final Chat chat;
  final VoidCallback? onTap;

  @override
  Widget build(BuildContext context) {
    return ListTile(
      onTap: onTap,
      leading: const Avatar(),
      title: Text('Conversation'),
      subtitle: Text(chat.lastMessage, maxLines: 1, overflow: TextOverflow.ellipsis),
      trailing: const Icon(Icons.chevron_right),
    );
  }
}
