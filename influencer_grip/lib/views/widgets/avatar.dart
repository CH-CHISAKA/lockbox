import 'package:flutter/material.dart';

class Avatar extends StatelessWidget {
  const Avatar({super.key, this.size = 40, this.imageUrl, this.initials});
  final double size;
  final String? imageUrl;
  final String? initials;

  @override
  Widget build(BuildContext context) {
    return CircleAvatar(
      radius: size / 2,
      backgroundImage: (imageUrl != null && imageUrl!.isNotEmpty) ? NetworkImage(imageUrl!) : null,
      child: (imageUrl == null || imageUrl!.isEmpty)
          ? Text(
              (initials ?? 'IG').substring(0, (initials ?? 'IG').length.clamp(0, 2)),
              style: const TextStyle(fontWeight: FontWeight.w600),
            )
          : null,
    );
  }
}
