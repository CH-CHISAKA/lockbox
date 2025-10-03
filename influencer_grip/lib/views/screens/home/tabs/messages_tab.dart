import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../../../controllers/chat_controller.dart';
import '../../../../models/chat.dart';
import '../../../widgets/chat_list_item.dart';
import '../../messages/chat_detail_screen.dart';

class MessagesTab extends StatelessWidget {
  const MessagesTab({super.key});

  @override
  Widget build(BuildContext context) {
    final controller = context.watch<ChatController>();
    final chats = controller.chats;

    return ListView.separated(
      padding: const EdgeInsets.all(16),
      itemCount: chats.length,
      separatorBuilder: (_, __) => const Divider(height: 1),
      itemBuilder: (context, index) {
        final chat = chats[index];
        return ChatListItem(
          chat: chat,
          onTap: () {
            Navigator.of(context).push(
              MaterialPageRoute(
                builder: (_) => ChangeNotifierProvider.value(
                  value: context.read<ChatController>(),
                  child: ChatDetailScreen(chatId: chat.id),
                ),
              ),
            );
          },
        );
      },
    );
  }
}
